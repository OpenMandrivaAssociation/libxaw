%define major 7
%define libname %mklibname xaw %{major}
%define devname %mklibname xaw -d

Name:		libxaw
Summary:	X Athena Widgets Library
Version:	1.0.12
Release:	2
Group:		System/Libraries
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
Patch0:		libXaw-1.0.10-formatstring.patch

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xpm) >= 3.5.4.2
BuildRequires:	pkgconfig(xt) >= 1.0.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.3.0
BuildRequires:	groff

%description
Xaw is the classic X Athena Widget Set, a widget set based on the
X Toolkit Intrinsics (Xt) Library.

%package -n %{libname}
Group:		System/Libraries
Summary:	X Athena Widgets Library
Requires:	x11-data-bitmaps
# (walluck):	FIXME:	we wouldn't provide this but for the packages that incorrectly require it
Provides:	libxaw7 = %{version}-%{release}

%description -n %{libname}
Xaw is the classic X Athena Widget Set, a widget set based on the
X Toolkit Intrinsics (Xt) Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	xaw-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXaw-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-xaw6

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXaw.so.%{major}
%{_libdir}/libXaw7.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*
%{_mandir}/man3/Xaw.3.*
%dir %{_docdir}/libXaw
%{_docdir}/libXaw/*

