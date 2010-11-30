%define libxaw7 %mklibname xaw 7
%define libxaw6 %mklibname xaw 6
%define libxawdevel %mklibname xaw -d
%define libxawstaticdevel %mklibname xaw -d -s

Name: libxaw
Summary: X Athena Widgets Library
Version: 1.0.8
Release: %mkrel 3
Group: System/Libraries
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2

Patch5: 0005-Correct-wrong-sprintf-call-using-variable-format.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: libxpm-devel >= 3.5.4.2
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.3.0
BuildRequires: groff

%description
Xaw is the classic X Athena Widget Set, a widget set based on the
X Toolkit Intrinsics (Xt) Library.

#-----------------------------------------------------------

%package -n %libxaw7
Group: System/Libraries
Summary: X Athena Widgets Library
Requires: x11-data-bitmaps
Conflicts: libxorg-x11 < 7.0
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Provides: libxaw7 = %{version}-%{release}

%description -n %libxaw7
Xaw is the classic X Athena Widget Set, a widget set based on the
X Toolkit Intrinsics (Xt) Library.

%if %mdkversion < 200900
%post -n %libxaw7 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libxaw7 -p /sbin/ldconfig
%endif

%files -n %libxaw7
%defattr(-,root,root)
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0

#-----------------------------------------------------------
%package -n %libxawdevel
Summary: Development files for %{name}
Group: Development/X11
Requires: %libxaw7 = %{version}-%{release}
Requires: libxmu-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Conflicts: libxorg-x11-devel < 7.0
Provides: xaw-devel = %{version}-%{release}
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Obsoletes: libxaw-devel < 1.0.3-5
Provides: libxaw-devel = %{version}-%{release}

%description -n %libxawdevel
Development files for %{name}.

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
%dir %{_docdir}/libXaw
%{_docdir}/libXaw/*

#-----------------------------------------------------------
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
Static development files for %{name}.

%files -n %libxawstaticdevel
%defattr(-,root,root)
%{_libdir}/*.a

#-----------------------------------------------------------

%prep
%setup -q -n libXaw-%{version}
%patch5 -p1

%build
%configure2_5x --disable-xaw6
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}
