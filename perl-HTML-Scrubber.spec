#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTML
%define		pnam	Scrubber
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::Scrubber - Perl extension for scrubbing/sanitizing HTML
Summary(pl.UTF-8):	HTML::Scrubber - rozszerzenie Perla do czyszczenia HTML-a
Name:		perl-HTML-Scrubber
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	79b5ab3a8e599d3753ed6bc924d0f501
URL:		http://search.cpan.org/dist/HTML-Scrubber/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-HTML-Parser >= 3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you wanna "scrub" or "sanitize" HTML input in a reliable and
flexible fashion, then this module is for you.

I wasn't satisfied with HTML::Sanitizer because it is based on
HTML::TreeBuilder, so I thought I'd write something similar that works
directly with HTML::Parser.

%description -l pl.UTF-8
Jeśli chcemy "oczyścić" albo "uporządkować" wejście w HTML w
wiarygodnym i elastycznym stylu, ten moduł ma zastosowanie.

Autor nie był usatysfakcjonowany HTML::Sanitizer, ponieważ jest oparty
na HTML::TreeBuilder, więc stwierdził, że napisze coś podobnego
działającego bezpośrednio z modułem HTML::Parser.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
