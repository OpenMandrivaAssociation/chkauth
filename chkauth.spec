Summary:	Script to change authentification method (local, NIS, LDAP)
Name:		chkauth
Version:	0.3
Release:	18
License:	GPLv2
Group:		System/Configuration/Boot and Init
Url:		www.openmandriva.org
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch

Requires:	perl >= 5.0

%description
Chkauth is a program to change the authentification method 
on a system. Chkauth always set the file method in first place, but 
you can only select the second authentification method this way. 

Three kind of authentification are accepted : local (file), NIS (yp) 
and LDAP. 

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_mandir}/man8/
mkdir -p %{buildroot}/%{_sbindir}
install chkauth %{buildroot}/%{_sbindir}
install chkauth.8 %{buildroot}/%{_mandir}/man8/

%files
%{_sbindir}/*
%{_mandir}/*/*

