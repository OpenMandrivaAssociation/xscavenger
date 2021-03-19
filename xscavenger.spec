%define name xscavenger
%define version 1.4.5
%define release  1
%define summary Cool arcade/thinking game very much like Lode Runner

Name: %{name}
Summary: %{summary}
Version: %{version}
Release: %{release}
Source: http://www.xdr.com/dash/%{name}-%{version}.tar.bz2
Source10: %{name}.16.png.bz2
Source11: %{name}.32.png.bz2
Source12: %{name}.48.png.bz2
#Patch0: xscavenger-1.4.4-link.patch
URL: http://www.xdr.com/dash/scavenger.html
License: GPL
Group: Games/Arcade
BuildRequires: pkgconfig(x11)
BuildRequires: imake

%description
Scavenger is a cool arcade/thinking game very much like Lode Runner.
You've got to run around and collect objects while avoiding enemies. Some
objects are buried and you've got to dig down to get at them. It's an
addictive game and some of the levels are devilishly (cruelly) complicated
to solve.

%prep
%setup -q
#patch0 -p0

%build
cd src
perl -pi -e 's,^LIBNAME.*,LIBNAME = %{_gamesdatadir}/%{name},' Imakefile
xmkmf
touch scavenger.man
make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT%{_gamesbindir} $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
cp src/scavenger $RPM_BUILD_ROOT%{_gamesbindir}
cp -a data/* $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
cp src/scavenger.6 $RPM_BUILD_ROOT%{_mandir}/man6

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/scavenger
Icon=%{name}
Categories=Game;ArcadeGame;
Name=X-Scavenger
Comment=%{summary}
EOF

mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
bzcat %{SOURCE10} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE11} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE12} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README DOC copyright
%attr(0755,root,root) %{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/*/*



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.4.4-10mdv2011.0
+ Revision: 634914
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.4.4-9mdv2010.0
+ Revision: 435275
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.4.4-8mdv2009.0
+ Revision: 262704
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.4.4-7mdv2009.0
+ Revision: 257710
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.4.4-5mdv2008.1
+ Revision: 135571
- BR imake
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xscavenger


* Sun Oct 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.4-5mdk
- BuildRequires fix

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.4-4mdk
- Rebuild

* Fri Feb 27 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.4-3mdk
- rebuild

* Tue Jan 14 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4.4-2mdk
- rebuild

* Sun Jan 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4.4-1mdk
- 1.4.4

* Wed Jun 12 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 143-2mdk
- png icons (out xpm!)

* Tue Mar 12 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 143-1mdk
- new version

* Mon Oct 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 142-3mdk
- fix obsolete-tag Copyright

* Thu Jul  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 142-2mdk
- rebuild
- add man page

* Thu Mar 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 142-1mdk
- first mdk release
