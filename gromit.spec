%define name gromit
%define version 0
%define cvs 20041213
%define release %mkrel %cvs.4

Summary: Paint annotations on top of the X screen
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.home.unix-ag.org/simon/gromit/%{name}-%{cvs}.tar.bz2
#gw work around for bug with lines filling all the screen
Patch0: gromit-20041213-no-history.patch
Patch1: gromit-20041213-fix-linking.patch
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
%autopatch -p1

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


%changelog
* Fri Nov 11 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0-20041213.4mdv2012.0
+ Revision: 730015
- fix linking
- rebuild

* Mon Nov 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0-20041213.3mdv2010.1
+ Revision: 463530
- update license
- work around a bug that filled the screen with lines

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0-20041213.2mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0-20041213.2mdv2008.0
+ Revision: 55231
- Import gromit



* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0-20041213.2mdv2007.0
- Rebuild

* Mon Apr 17 2006 Götz Waschk <waschk@mandriva.org> 0-20041213.1mdk
- rebuild

* Tue Apr 12 2005 Götz Waschk <waschk@linux-mandrake.com> 0-0.20041213.1mdk
- initial package
