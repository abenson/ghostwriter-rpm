#
# ghostwriter spec file
#
Summary: A distraction-free Markdown editor
Name: ghostwriter
Version: 1.5.0
Release: 1
License: GPL-3
Source: https://github.com/wereturtle/ghostwriter/archive/v1.5.0.tar.gz
URL: https://wereturtle.github.io/ghostwriter/
Packager: Andrew Benson <abenson+copr@gmail.com>

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	hunspell-devel
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtmultimedia-devel

Requires:	qt5-qtbase
Requires:	qt5-qtwebkit
Requires:	qt5-qtsvg
Requires:	qt5-qtmultimedia
Requires:	hunspell

%description
Enjoy a distraction-free writing experience, including a full screen 
mode and a clean interface. With Markdown, you can write now, and 
format later.

%build
qmake-qt5 -makefile PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
export INSTALL_ROOT=%{buildroot}
make install

%files
%{_bindir}/ghostwriter
%{_datarootdir}/ghostwriter/*
%{_datarootdir}/appdata/ghostwriter.appdata.xml
%{_datarootdir}/applications/ghostwriter.desktop
%{_datarootdir}/icons/hicolor/*/apps/ghostwriter.*
%{_datarootdir}/pixmaps/*
%{_mandir}/man1/*
%doc COPYING CREDITS.md

