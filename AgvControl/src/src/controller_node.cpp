#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class AGVController : public rclcpp::Node
{
public:
    AGVController() : Node("agv_controller")
    {
        // Publisher for wheel velocities (example topic)
        publisher_ = this->create_publisher<std_msgs::msg::String>("wheel_velocity", 10);
        
        // Timer to publish velocity commands every second
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1), std::bind(&AGVController::timer_callback, this));
    }

private:
    void timer_callback()
    {
        auto message = std_msgs::msg::String();
        message.data = "Set wheel velocities"; // Placeholder for actual velocity values
        publisher_->publish(message);
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<AGVController>());
    rclcpp::shutdown();
    return 0;
}
