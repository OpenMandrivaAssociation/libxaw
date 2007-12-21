%define libxaw8 %mklibname xaw 8
%define libxaw7 %mklibname xaw 7
%define libxaw6 %mklibname xaw 6
%define libxawdevel %mklibname xaw -d
%define libxawstaticdevel %mklibname xaw -d -s

%define	default_xprint	0

Name: libxaw
Summary: X Athena Widgets Library
Version: 1.0.4
Release: %mkrel 3
Group: System/Libraries
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
Patch0: 0001-fix-potential-infinte-loop-in-XawBoxQueryGeometry.patch
Patch1: 0002-default-no-xprint.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: libxpm-devel >= 3.5.4.2
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: ed

%description
X Athena Widgets Library.

#-----------------------------------------------------------

%package -n %libxaw8
Group: System/Libraries
Summary: Xaw version 8 library
Conflicts: libxorg-x11 < 7.0
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Provides: libxaw8 = %{version}-%{release}

%description -n %libxaw8
Xaw version 8 library

%post -n %libxaw8 -p /sbin/ldconfig
%postun -n %libxaw8 -p /sbin/ldconfig

%files -n %libxaw8
%defattr(-,root,root)
%{_libdir}/libXaw.so.8
%{_libdir}/libXaw8.so.8
%{_libdir}/libXaw8.so.8.0.0

#-----------------------------------------------------------

%package -n %libxaw7
Group: System/Libraries
Summary: Xaw version 7 library
Conflicts: libxorg-x11 < 7.0
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Provides: libxaw7 = %{version}-%{release}

%description -n %libxaw7
Xaw version 7 library

%post -n %libxaw7 -p /sbin/ldconfig
%postun -n %libxaw7 -p /sbin/ldconfig

%files -n %libxaw7
%defattr(-,root,root)
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0

#-----------------------------------------------------------

%package -n %libxaw6
Group: System/Libraries
Summary: Xaw version 6 library
Conflicts: libxorg-x11 < 7.0
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Provides: libxaw6 = %{version}-%{release}

%description -n %libxaw6
Xaw version 6 library

%post -n %libxaw6 -p /sbin/ldconfig
%postun -n %libxaw6 -p /sbin/ldconfig

%files -n %libxaw6
%defattr(-,root,root)
%{_libdir}/libXaw.so.6
%{_libdir}/libXaw6.so.6
%{_libdir}/libXaw6.so.6.0.1

#-----------------------------------------------------------

# (walluck): FIXME: this should be split into 4 packages: common, 6, 7, 8
%package -n %libxawdevel
Summary: Development files for %{name}
Group: Development/X11
Requires: %libxaw8 = %{version}-%{release}
Requires: %libxaw7 = %{version}-%{release}
Requires: %libxaw6 = %{version}-%{release}
Requires: libxmu-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Conflicts: libxorg-x11-devel < 7.0
Provides: xaw-devel = %{version}-%{release}
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Obsoletes: libxaw-devel < 1.0.3-5
Provides: libxaw-devel = %{version}-%{release}

%description -n %libxawdevel
Development files for %{name}

%pre -n %libxawdevel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %libxawdevel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*
%{_mandir}/man3/Xaw.3.*
%{_datadir}/aclocal/xaw.m4

#-----------------------------------------------------------

# (walluck): FIXME: this should be split into 3 packages: 6, 7, 8
%package -n %libxawstaticdevel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %libxawdevel = %{version}-%{release}
Provides: xaw-static-devel = %{version}-%{release}
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Obsoletes: libxaw-static-devel < 1.0.3-5
Provides: libxaw-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %libxawstaticdevel
Static development files for %{name}

%files -n %libxawstaticdevel
%defattr(-,root,root)
%{_libdir}/*.a

#-----------------------------------------------------------

%prep
%setup -q -n libXaw-%{version}
%patch0 -p1 -b .infinite-loop
%if !%{default_xprint}
%patch1 -p1 -b .no-xprint
%endif

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}
