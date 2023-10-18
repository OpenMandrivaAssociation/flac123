Summary:	Command line program for playing FLAC audio files
Name:		flac123
Version:	2.1.1
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://flac-tools.sourceforge.net/
Source0:  https://github.com/flac123/flac123/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#Source0:	http://downloads.sourceforge.net/project/flac-tools/flac123/%{name}-%{version}-release.tar.gz
Patch0:		flac123-no-Llib.patch
#Patch1:		flac123-compile.patch
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(flac) pkgconfig(ogg)

%description
%{name} is a command-line program for playing FLAC audio files.

%prep
%autosetup -p1
%configure

%build
%make_build CPPFLAGS=-DHAVE_INTTYPES_H

%install
%make_install

%files
%doc AUTHORS BUGS ChangeLog NEWS README*
%{_bindir}/*
