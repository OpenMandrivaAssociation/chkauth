%define name chkauth
%define version 0.3
%define release %mkrel 8
	
Summary: Script to change authentification method (local, NIS, LDAP)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch
License: GPL
Group: System/Configuration/Boot and Init
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
requires: perl >= 5.0

%description
Chkauth is a program to change the authentification method 
on a system. Chkauth always set the file method in first place, but 
you can only select the second authentification method this way. 

Three kind of authentification are accepted : local (file), NIS (yp) 
and LDAP. 

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_mandir}/man8/
mkdir -p %{buildroot}/%{_sbindir}
install chkauth %{buildroot}/%{_sbindir}
install chkauth.8 %{buildroot}/%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/*/*

