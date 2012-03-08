%define major 7
%define libxaw7 %mklibname xaw %{major}
%define develname %mklibname xaw -d

Name: libxaw
Summary: X Athena Widgets Library
Version: 1.0.9
Release: 4
Group: System/Libraries
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
Patch5: 0005-Correct-wrong-sprintf-call-using-variable-format.patch

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

%package -n %{libxaw7}
Group: System/Libraries
Summary: X Athena Widgets Library
Requires: x11-data-bitmaps
Conflicts: libxorg-x11 < 7.0
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Provides: libxaw7 = %{version}-%{release}

%description -n %{libxaw7}
Xaw is the classic X Athena Widget Set, a widget set based on the
X Toolkit Intrinsics (Xt) Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxaw7} = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Provides: xaw-devel = %{version}-%{release}
Provides: libxaw-devel = %{version}-%{release}
Obsoletes: %{_lib}xaw-static-devel

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXaw-%{version}
%patch5 -p1

%build
%configure2_5x \
	--disable-static \
	--disable-xaw6

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libxaw7}
%{_libdir}/libXaw.so.%{major}
%{_libdir}/libXaw7.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*
%{_mandir}/man3/Xaw.3.*
%dir %{_docdir}/libXaw
%{_docdir}/libXaw/*

