%define upstream_name    Dist-Zilla-Plugin-ChangelogFromGit
%define upstream_version 0.017

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Build CHANGES from git commits and tags
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rcaputo/dzp-changelogfromgit
Source0:	https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/Dist-Zilla-Plugin-ChangelogFromGit-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Text::Wrap)
BuildArch:	noarch

%description
This Dist::Zilla plugin writes a CHANGES file that contains formatted
commit information from recent git logs.

This plugin has the following configuration variables:

* * max_age

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml LICENSE CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

