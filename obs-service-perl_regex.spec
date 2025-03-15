%global service perl_regex

Name:           obs-service-%{service}
Version:        0.0.3
Release:        0
Summary:        Obs service that will do regex
License:        GPL-3.0-or-later
URL:            https://github.com/huakim/%{name}
Group:          Development/Tools/Building
BuildArch:      noarch
Source0:        %{service}
Source1:        %{service}.service

%(echo %{SOURCE0} | %{_rpmconfigdir}/perl.req | sed "s/^/Requires: /g")
Requires:       /usr/bin/perl
BuildRequires:  (rpm-build-perl or perl-generators or %{_rpmconfigdir}/perl.req)
BuildRequires:  rpm_macro(_obs_service_dir)
BuildRequires:  perl(Path::Tiny)

%description
%{summary}.

%install
%define file %{_obs_service_dir}/%{service}
%define script %{buildroot}%{file}
mkdir -p %{buildroot}%{_obs_service_dir}
cp %{SOURCE0} %{buildroot}%{file}
cp %{SOURCE1} %{buildroot}%{file}.service

%post
%postun

%files
%attr(755, root, root) %{file}
%attr(644, root, root) %{file}.service

%changelog
