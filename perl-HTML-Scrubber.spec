#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Scrubber
Summary:	HTML::Scrubber - Perl extension for scrubbing/sanitizing HTML
Summary(pl):	HTML::Scrubber - rozszerzenie Perla do czyszczenia HTML-a
Name:		perl-HTML-Scrubber
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abadf246e528f3e2d31717ef8a1d90f2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you wanna "scrub" or "sanitize" HTML input in a reliable and
flexible fashion, then this module is for you.

I wasn't satisfied with HTML::Sanitizer because it is based on
HTML::TreeBuilder, so I thought I'd write something similar that works
directly with HTML::Parser.

%description -l pl
Je¶li chcemy "oczy¶ciæ" albo "uporz±dkowaæ" wej¶cie w HTML w
wiarygodnym i elastycznym stylu, ten modu³ ma zastosowanie.

Autor nie by³ usatysfakcjonowany HTML::Sanitizer, poniewa¿ jest oparty
na HTML::TreeBuilder, wiêc stwierdzi³, ¿e napisze co¶ podobnego
dzia³aj±cego bezpo¶rednio z modu³em HTML::Parser.

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
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
