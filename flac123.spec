%define version 0.0.9
%define release %mkrel 5

Summary:	Command line program for playing FLAC audio files
Name:		flac123
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://flac-tools.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/flac-tools/%{name}-%{version}.tar.bz2
Patch0:		flac123-0.0.9-use-libao-default.patch
Patch1: flac123-0.0.9+flac-1.1.3.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libao-devel
BuildRequires:	popt-devel
BuildRequires:	libflac-devel libogg-devel

%description
%{name} is a command-line program for playing FLAC audio files.

%prep
%setup -q
%patch0 -p1 -b .libao-default
%patch1 -p1 -b .flac
aclocal-1.9
autoconf
automake-1.9

%build
%configure2_5x
%make CPPFLAGS=-DHAVE_INTTYPES_H

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog NEWS README*
%{_bindir}/*


