%define major 7
%define libxaw7 %mklibname xaw %{major}
%define develname %mklibname xaw -d

Name:		libxaw
Summary:	X Athena Widgets Library
Version:	1.0.11
Release:	2
Group:		System/Libraries
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
Patch0:		libXaw-1.0.10-formatstring.patch
Patch1:		xaw-aarch64.patch

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

%package -n %{libxaw7}
Group:		System/Libraries
Summary:	X Athena Widgets Library
Requires:	x11-data-bitmaps
Conflicts:	libxorg-x11 < 7.0
# (walluck): FIXME: we wouldn't provide this but for the packages that incorrectly require it
Provides:	libxaw7 = %{version}-%{release}

%description -n %{libxaw7}
Xaw is the classic X Athena Widget Set, a widget set based on the
X Toolkit Intrinsics (Xt) Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxaw7} = %{version}-%{release}
Conflicts:	libxorg-x11-devel < 7.0
Provides:	xaw-devel = %{version}-%{release}
Provides:	libxaw-devel = %{version}-%{release}
Obsoletes:	%{_lib}xaw-static-devel < 1.0.11

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXaw-%{version}
%patch0 -p1 -b .fs~
%patch1 -p1

%build
%configure2_5x \
	--disable-static \
	--disable-xaw6

%make

%install
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


%changelog
* Wed Jun 20 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.11-1
+ Revision: 806535
- drop patch 1, fixed upstream
- update to new version 1.0.11

* Tue May 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.10-2
+ Revision: 800154
- Correct a crash in xedit rebuilt with gcc 4.7.

* Thu Mar 29 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.0.10-1
+ Revision: 788265
- Update to 1.0.10

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.9-4
+ Revision: 783350
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.9-3
+ Revision: 745648
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-2
+ Revision: 661557
- mass rebuild

* Wed Jan 12 2011 Thierry Vignaud <tv@mandriva.org> 1.0.9-1
+ Revision: 630957
- new release

* Tue Nov 30 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.8-3mdv2011.0
+ Revision: 603747
- Improve package description
  The new description is based on the last release announcement email. It is
  almost the same text as the one inside the README file.
  CCBUG: 60966

* Mon Nov 29 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.8-2mdv2011.0
+ Revision: 603125
- Require x11-data-bitmaps
  libXaw assumes /usr/include/X11/bitmaps exists, see the documentation.
  This will remove warning messages that appear when starting some apps like xcalc
  and might also fix their appearance.

* Wed Oct 27 2010 Funda Wang <fwang@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 589554
- use configure switch to disalbe xaw6 build

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Tue Nov 24 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.7-2mdv2010.1
+ Revision: 469770
- Re-enable docs now that we have a working groff

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.7-1mdv2010.1
+ Revision: 464141
- Disable docs because our Groff can't compile them for now
- Fix spec

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Sat Jul 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.6-1mdv2010.0
+ Revision: 392297
- update to new version 1.0.6
- drop patches 1, 2, 3 and 4, were merged upstream

* Tue Feb 10 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.0.5-3mdv2009.1
+ Revision: 339293
- Remove dependency on libxaw6 from libxaw-devel.

* Tue Feb 10 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.0.5-2mdv2009.1
+ Revision: 339224
- o Correct bug found when enabling -Werror=format-security.
  o Disable build of libXaw6 by default, and don't generate the package.
  libXaw6 was mean't to ensure binary compatibility until packages were
  relinked with libXaw7.
  o Apply janitor/trivial patches required before the -Werror=format-security
  and disable of libxaw6.

  + Thierry Vignaud <tv@mandriva.org>
    - kill merged git patches
    - new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-5mdv2009.0
+ Revision: 223064
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-4mdv2008.1
+ Revision: 153295
- Update BuildRequires and rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 1.0.4-3mdv2008.1
+ Revision: 109209
- rebuild for new lzma

* Mon Oct 29 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2008.1
+ Revision: 103285
- Add patch.
- Default to not use xprint by default.
  The only sample implementation to use xprint was xedit, but since it was
  reverted to explicitly not use xprint, there is not reason to enable it by
  default on applications that don't use it.

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 68964
- new release

* Fri Aug 10 2007 David Walluck <walluck@mandriva.org> 1.0.3-5mdv2008.0
+ Revision: 61683
- fix devel upgrades by adding Obsoletes

* Fri Aug 10 2007 David Walluck <walluck@mandriva.org> 1.0.3-4mdv2008.0
+ Revision: 61655
- bring more in line with library policy
- document remaining library problems

* Mon Jul 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.3-3mdv2008.0
+ Revision: 52624
- Apply patch from Glenn Burkhardt <gbburkhardt@verizon.net> which fixes a
  potential integer overflow (fix #30370)

* Thu Jul 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 51464
- new version


* Sat Jan 27 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.2-5mdv2007.0
+ Revision: 114243
- rebuild and reupload

* Sun Aug 13 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0.2-4mdv2007.0
+ Revision: 55737
- add BuildRequires: ed - for a configure check that changes the sonames

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - Removed explicit provides for libraries
    - Provides libXa8.so.8
    - Provides libXa7.so.7
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix build on x86_64

