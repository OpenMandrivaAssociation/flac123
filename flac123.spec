%define version 0.0.11
%define release %mkrel 1

Summary:	Command line program for playing FLAC audio files
Name:		flac123
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://flac-tools.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/flac-tools/%{name}-%{version}.tar.bz2
BuildRequires:	libao-devel
BuildRequires:	popt-devel
BuildRequires:	libflac-devel libogg-devel

%description
%{name} is a command-line program for playing FLAC audio files.

%prep
%setup -q

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


