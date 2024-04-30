%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-desktop
Version:        0.11.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS desktop package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-action-tutorials-cpp
Requires:       ros-jazzy-action-tutorials-interfaces
Requires:       ros-jazzy-action-tutorials-py
Requires:       ros-jazzy-angles
Requires:       ros-jazzy-composition
Requires:       ros-jazzy-demo-nodes-cpp
Requires:       ros-jazzy-demo-nodes-cpp-native
Requires:       ros-jazzy-demo-nodes-py
Requires:       ros-jazzy-depthimage-to-laserscan
Requires:       ros-jazzy-dummy-map-server
Requires:       ros-jazzy-dummy-robot-bringup
Requires:       ros-jazzy-dummy-sensors
Requires:       ros-jazzy-examples-rclcpp-minimal-action-client
Requires:       ros-jazzy-examples-rclcpp-minimal-action-server
Requires:       ros-jazzy-examples-rclcpp-minimal-client
Requires:       ros-jazzy-examples-rclcpp-minimal-composition
Requires:       ros-jazzy-examples-rclcpp-minimal-publisher
Requires:       ros-jazzy-examples-rclcpp-minimal-service
Requires:       ros-jazzy-examples-rclcpp-minimal-subscriber
Requires:       ros-jazzy-examples-rclcpp-minimal-timer
Requires:       ros-jazzy-examples-rclcpp-multithreaded-executor
Requires:       ros-jazzy-examples-rclpy-executors
Requires:       ros-jazzy-examples-rclpy-minimal-action-client
Requires:       ros-jazzy-examples-rclpy-minimal-action-server
Requires:       ros-jazzy-examples-rclpy-minimal-client
Requires:       ros-jazzy-examples-rclpy-minimal-publisher
Requires:       ros-jazzy-examples-rclpy-minimal-service
Requires:       ros-jazzy-examples-rclpy-minimal-subscriber
Requires:       ros-jazzy-image-tools
Requires:       ros-jazzy-intra-process-demo
Requires:       ros-jazzy-joy
Requires:       ros-jazzy-lifecycle
Requires:       ros-jazzy-logging-demo
Requires:       ros-jazzy-pcl-conversions
Requires:       ros-jazzy-pendulum-control
Requires:       ros-jazzy-pendulum-msgs
Requires:       ros-jazzy-quality-of-service-demo-cpp
Requires:       ros-jazzy-quality-of-service-demo-py
Requires:       ros-jazzy-ros-base
Requires:       ros-jazzy-rqt-common-plugins
Requires:       ros-jazzy-rviz-default-plugins
Requires:       ros-jazzy-rviz2
Requires:       ros-jazzy-teleop-twist-joy
Requires:       ros-jazzy-teleop-twist-keyboard
Requires:       ros-jazzy-tlsf
Requires:       ros-jazzy-tlsf-cpp
Requires:       ros-jazzy-topic-monitor
Requires:       ros-jazzy-turtlesim
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ros-workspace
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
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
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Tue Apr 30 2024 Geoffrey Biggs <geoff@openrobotics.org> - 0.11.0-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Steven! Ragnarök <steven@openrobotics.org> - 0.10.0-4
- Autogenerated by Bloom

* Wed Mar 06 2024 Steven! Ragnarök <steven@openrobotics.org> - 0.10.0-3
- Autogenerated by Bloom

