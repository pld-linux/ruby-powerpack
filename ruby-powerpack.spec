#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	powerpack
Summary:	A few useful extensions to core Ruby classes
Name:		ruby-%{pkgname}
Version:	0.1.2
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	745bf5d0bc2766b0d193d01b95d01acf
URL:		https://github.com/bbatsov/powerpack
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.13
BuildRequires:	ruby-yard < 1
BuildRequires:	ruby-yard >= 0.8
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A few useful extensions to core Ruby classes.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
