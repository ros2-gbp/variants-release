%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-desktop
Version:        0.11.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS desktop package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-action-tutorials-cpp
Requires:       ros-rolling-action-tutorials-interfaces
Requires:       ros-rolling-action-tutorials-py
Requires:       ros-rolling-angles
Requires:       ros-rolling-composition
Requires:       ros-rolling-demo-nodes-cpp
Requires:       ros-rolling-demo-nodes-cpp-native
Requires:       ros-rolling-demo-nodes-py
Requires:       ros-rolling-depthimage-to-laserscan
Requires:       ros-rolling-dummy-map-server
Requires:       ros-rolling-dummy-robot-bringup
Requires:       ros-rolling-dummy-sensors
Requires:       ros-rolling-examples-rclcpp-minimal-action-client
Requires:       ros-rolling-examples-rclcpp-minimal-action-server
Requires:       ros-rolling-examples-rclcpp-minimal-client
Requires:       ros-rolling-examples-rclcpp-minimal-composition
Requires:       ros-rolling-examples-rclcpp-minimal-publisher
Requires:       ros-rolling-examples-rclcpp-minimal-service
Requires:       ros-rolling-examples-rclcpp-minimal-subscriber
Requires:       ros-rolling-examples-rclcpp-minimal-timer
Requires:       ros-rolling-examples-rclcpp-multithreaded-executor
Requires:       ros-rolling-examples-rclpy-executors
Requires:       ros-rolling-examples-rclpy-minimal-action-client
Requires:       ros-rolling-examples-rclpy-minimal-action-server
Requires:       ros-rolling-examples-rclpy-minimal-client
Requires:       ros-rolling-examples-rclpy-minimal-publisher
Requires:       ros-rolling-examples-rclpy-minimal-service
Requires:       ros-rolling-examples-rclpy-minimal-subscriber
Requires:       ros-rolling-image-tools
Requires:       ros-rolling-intra-process-demo
Requires:       ros-rolling-joy
Requires:       ros-rolling-lifecycle
Requires:       ros-rolling-logging-demo
Requires:       ros-rolling-pcl-conversions
Requires:       ros-rolling-pendulum-control
Requires:       ros-rolling-pendulum-msgs
Requires:       ros-rolling-quality-of-service-demo-cpp
Requires:       ros-rolling-quality-of-service-demo-py
Requires:       ros-rolling-ros-base
Requires:       ros-rolling-rqt-common-plugins
Requires:       ros-rolling-rviz-default-plugins
Requires:       ros-rolling-rviz2
Requires:       ros-rolling-teleop-twist-joy
Requires:       ros-rolling-teleop-twist-keyboard
Requires:       ros-rolling-tlsf
Requires:       ros-rolling-tlsf-cpp
Requires:       ros-rolling-topic-monitor
Requires:       ros-rolling-turtlesim
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ros-workspace
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
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
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
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Apr 30 2024 Geoffrey Biggs <geoff@openrobotics.org> - 0.11.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Steven! Ragnarök <steven@openrobotics.org> - 0.10.0-3
- Autogenerated by Bloom

