# BlackRobots Foundation Jekyll Gemfile
source "https://rubygems.org"

# Jekyll version
gem "jekyll", "~> 4.3.3"

# Default theme
gem "jekyll-theme-primer", "~> 0.6.0"

# Essential plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
  gem "jekyll-responsive-image"
  gem "jekyll-minifier"
  gem "jekyll-compress-images"
end

# Windows and JRuby does not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# Development dependencies
group :development do
  gem "webrick", "~> 1.7"
end