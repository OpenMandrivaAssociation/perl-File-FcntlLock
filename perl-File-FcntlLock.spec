%define upstream_name    File-FcntlLock
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:    File locking with fcntl()
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Errno)
BuildRequires: perl(Exporter)
BuildRequires: perl(POSIX)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
File locking in Perl is usually done using the the flock() manpage
function. Unfortunately, this only allows locks on whole files and is often
implemented in terms of the flock(2) manpage, which has some shortcomings.

Using this module file locking via the fcntl(2) manpage can be done
(obviously, this restricts the use of the module to systems that have a the
fcntl(2) manpage system call). Before a file (or parts of a file) can be
locked, an object simulating a flock structure must be created and its
properties set. Afterwards, by calling the 'lock()' method a lock can be
set or it can be determined if and which process currently holds the lock.

To create a new object representing a flock structure call 'new()':

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-6mdv2012.0
+ Revision: 765239
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-5
+ Revision: 763752
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-4
+ Revision: 667139
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.120.0-3mdv2011.0
+ Revision: 564434
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 555251
- rebuild

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 483878
- import perl-File-FcntlLock


* Wed Dec 30 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
