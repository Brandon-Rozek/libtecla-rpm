Name:     libtecla
Version:  1.6.3
Release:  %autorelease
Summary:  Command-line editing library
License:  X11
URL:      https://sites.astro.caltech.edu/~mcs/tecla/
Source:   https://sites.astro.caltech.edu/~mcs/tecla/libtecla-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  bash
BuildRequires:  ncurses-devel

Patch0: libtecla-1.6.3-destdir.patch
Patch1: libtecla-1.6.3-build-id.patch

%description
The tecla library provides UNIX and LINUX programs with interactive command line
editing facilities, similar to those of the UNIX tcsh shell.
In addition to simple command-line editing, it supports recall of previously
entered command lines, TAB completion of file names or other tokens,
and in-line wild-card expansion of filenames.

%prep
%setup -q -n libtecla

%patch -P 0 -p0
%patch -P 1 -p0

%build



%configure
%make_build

%install
%make_install

# Unneeded files
rm %{buildroot}/usr/bin/enhance
rm %{buildroot}/usr/share/man/man1/enhance.1
rm %{buildroot}/usr/lib64/libtecla_r.a
rm %{buildroot}/usr/lib64/libtecla_r.so
rm %{buildroot}/usr/lib64/libtecla_r.so.1
rm %{buildroot}/usr/lib64/libtecla_r.so.1.6.3


%files
%{_libdir}/libtecla.a
%{_libdir}/libtecla.so.1.6.3
%{_libdir}/libtecla.so
%{_libdir}/libtecla.so.1

%{_includedir}/libtecla.h
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%license LICENSE.TERMS
%doc README PORTING RELEASE.NOTES CHANGES

%changelog
%autochangelog
