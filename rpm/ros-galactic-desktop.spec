%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-desktop
Version:        0.9.3
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS desktop package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-action-tutorials-cpp
Requires:       ros-galactic-action-tutorials-interfaces
Requires:       ros-galactic-action-tutorials-py
Requires:       ros-galactic-angles
Requires:       ros-galactic-composition
Requires:       ros-galactic-demo-nodes-cpp
Requires:       ros-galactic-demo-nodes-cpp-native
Requires:       ros-galactic-demo-nodes-py
Requires:       ros-galactic-depthimage-to-laserscan
Requires:       ros-galactic-dummy-map-server
Requires:       ros-galactic-dummy-robot-bringup
Requires:       ros-galactic-dummy-sensors
Requires:       ros-galactic-examples-rclcpp-minimal-action-client
Requires:       ros-galactic-examples-rclcpp-minimal-action-server
Requires:       ros-galactic-examples-rclcpp-minimal-client
Requires:       ros-galactic-examples-rclcpp-minimal-composition
Requires:       ros-galactic-examples-rclcpp-minimal-publisher
Requires:       ros-galactic-examples-rclcpp-minimal-service
Requires:       ros-galactic-examples-rclcpp-minimal-subscriber
Requires:       ros-galactic-examples-rclcpp-minimal-timer
Requires:       ros-galactic-examples-rclcpp-multithreaded-executor
Requires:       ros-galactic-examples-rclpy-executors
Requires:       ros-galactic-examples-rclpy-minimal-action-client
Requires:       ros-galactic-examples-rclpy-minimal-action-server
Requires:       ros-galactic-examples-rclpy-minimal-client
Requires:       ros-galactic-examples-rclpy-minimal-publisher
Requires:       ros-galactic-examples-rclpy-minimal-service
Requires:       ros-galactic-examples-rclpy-minimal-subscriber
Requires:       ros-galactic-image-tools
Requires:       ros-galactic-intra-process-demo
Requires:       ros-galactic-joy
Requires:       ros-galactic-lifecycle
Requires:       ros-galactic-logging-demo
Requires:       ros-galactic-pcl-conversions
Requires:       ros-galactic-pendulum-control
Requires:       ros-galactic-pendulum-msgs
Requires:       ros-galactic-quality-of-service-demo-cpp
Requires:       ros-galactic-quality-of-service-demo-py
Requires:       ros-galactic-ros-base
Requires:       ros-galactic-rqt-common-plugins
Requires:       ros-galactic-rviz-default-plugins
Requires:       ros-galactic-rviz2
Requires:       ros-galactic-teleop-twist-joy
Requires:       ros-galactic-teleop-twist-keyboard
Requires:       ros-galactic-tlsf
Requires:       ros-galactic-tlsf-cpp
Requires:       ros-galactic-topic-monitor
Requires:       ros-galactic-turtlesim
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ros-workspace
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
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Apr 20 2021 Steven! Ragnarök <steven@openrobotics.org> - 0.9.3-2
- Autogenerated by Bloom

* Thu Mar 18 2021 Steven! Ragnarök <steven@openrobotics.org> - 0.9.3-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Steven! Ragnarök <steven@openrobotics.org> - 0.9.2-1
- Autogenerated by Bloom

