%define name chkauth
%define version 0.3
%define release %mkrel 5
	
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8/
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install chkauth $RPM_BUILD_ROOT/%{_sbindir}
install chkauth.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/*/*

