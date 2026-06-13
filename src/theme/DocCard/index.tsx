import React, {type ReactNode} from 'react';
import {
  useDocById,
  findFirstSidebarItemLink,
} from '@docusaurus/plugin-content-docs/client';
import {
  extractLeadingEmoji,
  useDocCardDescriptionCategoryItemsPlural,
} from '@docusaurus/theme-common/internal';
import isInternalUrl from '@docusaurus/isInternalUrl';
import {useBaseUrlUtils} from '@docusaurus/useBaseUrl';
import Layout from '@theme/DocCard/Layout';

import type {Props} from '@theme/DocCard';
import type {
  PropSidebarItemCategory,
  PropSidebarItemLink,
} from '@docusaurus/plugin-content-docs';

function getFallbackEmojiIcon(
  item: PropSidebarItemLink | PropSidebarItemCategory,
): string {
  if (item.type === 'category') {
    return '🗃';
  }
  return isInternalUrl(item.href) ? '📄️' : '🔗';
}

// Detecta si el icono personalizado es una ruta de imagen (SVG, PNG, etc.)
function isImagePath(value: string): boolean {
  return /\.(svg|png|jpe?g|gif|webp)$/i.test(value) || value.startsWith('/');
}

function getIconTitleProps(
  item: PropSidebarItemLink | PropSidebarItemCategory,
): {icon: ReactNode; title: string} {
  const {withBaseUrl} = useBaseUrlUtils();
  const extracted = extractLeadingEmoji(item.label);
  const title = extracted.rest.trim();

  // Icono propio definido en el frontmatter (sidebar_custom_props.icon)
  // o en _category_.json (customProps.icon). Puede ser un emoji o una ruta de imagen.
  const customIcon = item.customProps?.icon as string | undefined;
  if (customIcon) {
    if (isImagePath(customIcon)) {
      return {
        icon: (
          <img src={withBaseUrl(customIcon)} alt="" width={24} height={24} />
        ),
        title,
      };
    }
    return {icon: customIcon, title};
  }

  const emoji = extracted.emoji ?? getFallbackEmojiIcon(item);
  return {
    icon: emoji,
    title,
  };
}

function CardCategory({item}: {item: PropSidebarItemCategory}): ReactNode {
  const href = findFirstSidebarItemLink(item);
  const categoryItemsPlural = useDocCardDescriptionCategoryItemsPlural();

  // Unexpected: categories that don't have a link have been filtered upfront
  if (!href) {
    return null;
  }
  return (
    <Layout
      item={item}
      className={item.className}
      href={href}
      description={item.description ?? categoryItemsPlural(item.items.length)}
      {...getIconTitleProps(item)}
    />
  );
}

function CardLink({item}: {item: PropSidebarItemLink}): ReactNode {
  const doc = useDocById(item.docId ?? undefined);
  return (
    <Layout
      item={item}
      className={item.className}
      href={item.href}
      description={item.description ?? doc?.description}
      {...getIconTitleProps(item)}
    />
  );
}

export default function DocCard({item}: Props): ReactNode {
  switch (item.type) {
    case 'link':
      return <CardLink item={item} />;
    case 'category':
      return <CardCategory item={item} />;
    default:
      throw new Error(`unknown item type ${JSON.stringify(item)}`);
  }
}
