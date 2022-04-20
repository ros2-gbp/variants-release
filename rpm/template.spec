%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-desktop
Version:        0.9.3
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS desktop package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-action-tutorials-cpp
Requires:       ros-humble-action-tutorials-interfaces
Requires:       ros-humble-action-tutorials-py
Requires:       ros-humble-angles
Requires:       ros-humble-composition
Requires:       ros-humble-demo-nodes-cpp
Requires:       ros-humble-demo-nodes-cpp-native
Requires:       ros-humble-demo-nodes-py
Requires:       ros-humble-depthimage-to-laserscan
Requires:       ros-humble-dummy-map-server
Requires:       ros-humble-dummy-robot-bringup
Requires:       ros-humble-dummy-sensors
Requires:       ros-humble-examples-rclcpp-minimal-action-client
Requires:       ros-humble-examples-rclcpp-minimal-action-server
Requires:       ros-humble-examples-rclcpp-minimal-client
Requires:       ros-humble-examples-rclcpp-minimal-composition
Requires:       ros-humble-examples-rclcpp-minimal-publisher
Requires:       ros-humble-examples-rclcpp-minimal-service
Requires:       ros-humble-examples-rclcpp-minimal-subscriber
Requires:       ros-humble-examples-rclcpp-minimal-timer
Requires:       ros-humble-examples-rclcpp-multithreaded-executor
Requires:       ros-humble-examples-rclpy-executors
Requires:       ros-humble-examples-rclpy-minimal-action-client
Requires:       ros-humble-examples-rclpy-minimal-action-server
Requires:       ros-humble-examples-rclpy-minimal-client
Requires:       ros-humble-examples-rclpy-minimal-publisher
Requires:       ros-humble-examples-rclpy-minimal-service
Requires:       ros-humble-examples-rclpy-minimal-subscriber
Requires:       ros-humble-image-tools
Requires:       ros-humble-intra-process-demo
Requires:       ros-humble-joy
Requires:       ros-humble-lifecycle
Requires:       ros-humble-logging-demo
Requires:       ros-humble-pcl-conversions
Requires:       ros-humble-pendulum-control
Requires:       ros-humble-pendulum-msgs
Requires:       ros-humble-quality-of-service-demo-cpp
Requires:       ros-humble-quality-of-service-demo-py
Requires:       ros-humble-ros-base
Requires:       ros-humble-rqt-common-plugins
Requires:       ros-humble-rviz-default-plugins
Requires:       ros-humble-rviz2
Requires:       ros-humble-teleop-twist-joy
Requires:       ros-humble-teleop-twist-keyboard
Requires:       ros-humble-tlsf
Requires:       ros-humble-tlsf-cpp
Requires:       ros-humble-topic-monitor
Requires:       ros-humble-turtlesim
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A package which extends 'ros_base' and includes high level packages like
vizualization tools and demos.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Apr 19 2022 Steven! Ragnarök <steven@openrobotics.org> - 0.9.3-3
- Autogenerated by Bloom

* Tue Feb 08 2022 Steven! Ragnarök <steven@openrobotics.org> - 0.9.3-2
- Autogenerated by Bloom

