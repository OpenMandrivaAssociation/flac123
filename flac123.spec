%define version 0.0.12
%define release %mkrel 1

Summary:	Command line program for playing FLAC audio files
Name:		flac123
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Sound
URL:		http://flac-tools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/flac-tools/flac123/%{name}-%{version}-release.tar.gz
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(flac) pkgconfig(ogg)

%description
%{name} is a command-line program for playing FLAC audio files.

%prep
%setup -q

%build
%configure2_5x
%make CPPFLAGS=-DHAVE_INTTYPES_H

%install
%makeinstall_std

%files
%doc AUTHORS BUGS ChangeLog NEWS README*
%{_bindir}/*
