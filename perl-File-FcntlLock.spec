%define modname	File-FcntlLock
%define modver 0.22

Summary:	File locking with fcntl()

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(POSIX)
BuildRequires:	perl-devel

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
%autosetup -n %{modname}-%{modver} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
%make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorarch}/*
%{_mandir}/man3/*
