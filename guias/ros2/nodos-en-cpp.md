---
sidebar_position: 9
title: Nodos en C++
sidebar_custom_props:
  icon: /img/guias/iconos/codigo.svg
---

# Nodos en C++

Python es la forma más rápida de escribir un nodo. **C++** es la que usan los nodos que necesitan la máxima velocidad: drivers de sensores, control de motores a alta frecuencia, procesamiento de nubes de puntos. Los dos se entienden perfectamente entre sí: un nodo en C++ publica y uno en Python escucha, como en la [prueba de la instalación](./instalacion#5-comprobar-que-funciona).

| | Python (`rclpy`) | C++ (`rclcpp`) |
|---|---|---|
| Escribir y probar | muy rápido | más lento |
| Velocidad de ejecución | suficiente para casi todo | máxima |
| Compilar | no hace falta | sí, con CMake |
| Uso típico | lógica, prototipos, IA | drivers, control, percepción |

Vamos a escribir el mismo [dibujante](./primer-paquete) de la tortuga, ahora en C++.

## 1. El paquete

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake mi_robot_cpp --dependencies rclcpp geometry_msgs
```

## 2. El nodo

Crea `~/ros2_ws/src/mi_robot_cpp/src/dibujante.cpp`:

```cpp
#include <chrono>
#include <memory>

#include "geometry_msgs/msg/twist.hpp"
#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class Dibujante : public rclcpp::Node
{
public:
  Dibujante()
  : Node("dibujante_cpp")
  {
    velocidad_ = declare_parameter("velocidad", 2.0);
    giro_ = declare_parameter("giro", 1.0);
    publicador_ = create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
    timer_ = create_wall_timer(100ms, [this]() {publicar();});
    RCLCPP_INFO(get_logger(), "Dibujante en C++ en marcha");
  }

private:
  void publicar()
  {
    geometry_msgs::msg::Twist msg;
    msg.linear.x = velocidad_;
    msg.angular.z = giro_;
    publicador_->publish(msg);
  }

  double velocidad_;
  double giro_;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publicador_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Dibujante>());
  rclcpp::shutdown();
  return 0;
}
```

Es el mismo nodo que en Python, pieza a pieza:

| Python | C++ |
|---|---|
| `class Dibujante(Node)` | `class Dibujante : public rclcpp::Node` |
| `create_publisher(Twist, ...)` | `create_publisher<geometry_msgs::msg::Twist>(...)` |
| `create_timer(0.1, self.publicar)` | `create_wall_timer(100ms, [this]() {publicar();})` |
| `self.get_logger().info(...)` | `RCLCPP_INFO(get_logger(), ...)` |
| `declare_parameter('giro', 1.0)` | `declare_parameter("giro", 1.0)` |
| `rclpy.spin(nodo)` | `rclcpp::spin(...)` |

## 3. Decirle a CMake qué compilar

Sustituye `~/ros2_ws/src/mi_robot_cpp/CMakeLists.txt` por:

```cmake
cmake_minimum_required(VERSION 3.8)
project(mi_robot_cpp)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(dibujante src/dibujante.cpp)
ament_target_dependencies(dibujante rclcpp geometry_msgs)

install(TARGETS dibujante
  DESTINATION lib/${PROJECT_NAME})

ament_package()
```

- `add_executable` crea el programa a partir del archivo
- `ament_target_dependencies` lo enlaza con las librerías de ROS 2
- `install` lo copia donde `ros2 run` lo busca

## 4. Compilar y probar

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 run mi_robot_cpp dibujante
```

Con `turtlesim_node` en marcha, la tortuga dibuja su círculo, ahora movida por un nodo en C++. Los parámetros funcionan igual:

```bash
ros2 param get /dibujante_cpp giro
```

```
Double value is: 1.0
```

:::tip
Al compilar puede aparecer un aviso de CMake sobre la versión mínima (`Compatibility with CMake < 3.10`). Es normal en sistemas con un CMake reciente y no afecta al resultado.
:::

:::note
Para compilar un solo paquete cuando el workspace crece: `colcon build --packages-select mi_robot_cpp`.
:::
