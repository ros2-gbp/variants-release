%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/kilted/.*$
%global __requires_exclude_from ^/opt/ros/kilted/.*$

%global __cmake_in_source_build 1

Name:           ros-kilted-desktop
Version:        0.12.0
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS desktop package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kilted-action-tutorials-cpp
Requires:       ros-kilted-action-tutorials-py
Requires:       ros-kilted-angles
Requires:       ros-kilted-composition
Requires:       ros-kilted-demo-nodes-cpp
Requires:       ros-kilted-demo-nodes-cpp-native
Requires:       ros-kilted-demo-nodes-py
Requires:       ros-kilted-depthimage-to-laserscan
Requires:       ros-kilted-dummy-map-server
Requires:       ros-kilted-dummy-robot-bringup
Requires:       ros-kilted-dummy-sensors
Requires:       ros-kilted-examples-rclcpp-minimal-action-client
Requires:       ros-kilted-examples-rclcpp-minimal-action-server
Requires:       ros-kilted-examples-rclcpp-minimal-client
Requires:       ros-kilted-examples-rclcpp-minimal-composition
Requires:       ros-kilted-examples-rclcpp-minimal-publisher
Requires:       ros-kilted-examples-rclcpp-minimal-service
Requires:       ros-kilted-examples-rclcpp-minimal-subscriber
Requires:       ros-kilted-examples-rclcpp-minimal-timer
Requires:       ros-kilted-examples-rclcpp-multithreaded-executor
Requires:       ros-kilted-examples-rclpy-executors
Requires:       ros-kilted-examples-rclpy-minimal-action-client
Requires:       ros-kilted-examples-rclpy-minimal-action-server
Requires:       ros-kilted-examples-rclpy-minimal-client
Requires:       ros-kilted-examples-rclpy-minimal-publisher
Requires:       ros-kilted-examples-rclpy-minimal-service
Requires:       ros-kilted-examples-rclpy-minimal-subscriber
Requires:       ros-kilted-image-tools
Requires:       ros-kilted-intra-process-demo
Requires:       ros-kilted-joy
Requires:       ros-kilted-lifecycle
Requires:       ros-kilted-logging-demo
Requires:       ros-kilted-pcl-conversions
Requires:       ros-kilted-pendulum-control
Requires:       ros-kilted-pendulum-msgs
Requires:       ros-kilted-quality-of-service-demo-cpp
Requires:       ros-kilted-quality-of-service-demo-py
Requires:       ros-kilted-ros-base
Requires:       ros-kilted-rqt-common-plugins
Requires:       ros-kilted-rviz-default-plugins
Requires:       ros-kilted-rviz2
Requires:       ros-kilted-teleop-twist-joy
Requires:       ros-kilted-teleop-twist-keyboard
Requires:       ros-kilted-tlsf
Requires:       ros-kilted-tlsf-cpp
Requires:       ros-kilted-topic-monitor
Requires:       ros-kilted-turtlesim
Requires:       ros-kilted-ros-workspace
BuildRequires:  ros-kilted-ament-cmake
BuildRequires:  ros-kilted-ros-workspace
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
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/kilted" \
    -DAMENT_PREFIX_PATH="/opt/ros/kilted" \
    -DCMAKE_PREFIX_PATH="/opt/ros/kilted" \
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
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kilted/setup.sh" ]; then . "/opt/ros/kilted/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/kilted

%changelog
* Wed Apr 23 2025 Geoffrey Biggs <geoff@openrobotics.org> - 0.12.0-2
- Autogenerated by Bloom

* Wed Oct 09 2024 Geoffrey Biggs <geoff@openrobotics.org> - 0.12.0-1
- Autogenerated by Bloom

* Tue Apr 30 2024 Geoffrey Biggs <geoff@openrobotics.org> - 0.11.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Steven! Ragnarök <steven@openrobotics.org> - 0.10.0-3
- Autogenerated by Bloom

