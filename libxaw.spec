%define libxaw8 %mklibname xaw 8
%define libxaw7 %mklibname xaw 7
%define libxaw6 %mklibname xaw 6

Name: libxaw
Summary: X Athena Widgets Library
Version: 1.0.3
Release: %mkrel 1
Group: System/Libraries
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

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
Provides: libxaw8 = %{version}

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
Provides: libxaw7 = %{version}

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
Provides: libxaw6 = %{version}

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

%package devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %libxaw8 = %{version}
Requires: %libxaw7 = %{version}
Requires: %libxaw6 = %{version}
Requires: libxmu-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Conflicts: libxorg-x11-devel < 7.0

%description devel
Development files for %{name}

%pre devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*
%{_mandir}/man3/Xaw.3x.bz2
%{_datadir}/aclocal/xaw.m4

#-----------------------------------------------------------

%package static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{name}-devel >= %{version}
Provides: libxawname-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description static-devel
Static development files for %{name}

%files static-devel
%defattr(-,root,root)
%{_libdir}/*.a

#-----------------------------------------------------------

%prep
%setup -q -n libXaw-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}
