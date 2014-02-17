#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	powerpack
Summary:	A few useful extensions to core Ruby classes
Name:		ruby-%{pkgname}
Version:	0.0.9
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1882a5be5c2cf10a78052b8f262be5f6
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}