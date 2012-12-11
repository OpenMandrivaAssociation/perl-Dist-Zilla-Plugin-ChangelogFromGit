%define upstream_name    Dist-Zilla-Plugin-ChangelogFromGit
%define upstream_version 0.002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Build CHANGES from git commits and tags
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

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

