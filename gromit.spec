%define name gromit
%define version 0
%define cvs 20041213
%define release %mkrel %cvs.3

Summary: Paint annotations on top of the X screen
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.home.unix-ag.org/simon/gromit/%{name}-%{cvs}.tar.bz2
#gw work around for bug with lines filling all the screen
Patch: gromit-20041213-no-history.patch
License: GPLv2+
Group: System/X11
Url: http://www.home.unix-ag.org/simon/gromit/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel

%description
Gromit (GRaphics Over MIscellaneous Things) is a small tool to make
annotations on the screen.

It is useful for recording presentations with xvidcap.

%prep
%setup -q -n %name-%cvs
%patch -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D %name %buildroot%_bindir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_bindir/%name
