%define name xscavenger
%define version 1.4.4
%define release %mkrel 9
%define summary Cool arcade/thinking game very much like Lode Runner

Name: %{name}
Summary: %{summary}
Version: %{version}
Release: %{release}
Source: http://www.xdr.com/dash/%{name}-%{version}.tar.bz2
Source10: %{name}.16.png.bz2
Source11: %{name}.32.png.bz2
Source12: %{name}.48.png.bz2
URL: http://www.xdr.com/dash/scavenger.html
License: GPL
Group: Games/Arcade
BuildRequires: X11-devel imake
BuildRequires: xorg-x11
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Scavenger is a cool arcade/thinking game very much like Lode Runner.
You've got to run around and collect objects while avoiding enemies. Some
objects are buried and you've got to dig down to get at them. It's an
addictive game and some of the levels are devilishly (cruelly) complicated
to solve.

%prep
%setup -q

%build
cd src
perl -pi -e 's,^LIBNAME.*,LIBNAME = %{_gamesdatadir}/%{name},' Imakefile
xmkmf
touch scavenger.man
make

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

