#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Package
%define	pnam	Generator
Summary:	Package::Generator - generate new packages quickly and easily
Summary(pl.UTF-8):	Package::Generator - szybkie i łatwe generowanie nowych pakietów
Name:		perl-Package-Generator
Version:	0.100
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Package/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	201e8aec3f37b879bd01abd5ad22fe5e
URL:		http://search.cpan.org/dist/Package-Generator/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you quickly and easily construct new packages. It
gives them unused names and sets up their package data, if provided.

%description -l pl.UTF-8
Ten moduł pozwala szybko i łatwo konstruować nowe pakiety. Nadaje im
unikalne nazwy i w razie potrzeby konfiguruje dane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Package/*.pm
%{_mandir}/man3/*