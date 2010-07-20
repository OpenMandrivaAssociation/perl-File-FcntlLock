%define upstream_name    File-FcntlLock
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

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


