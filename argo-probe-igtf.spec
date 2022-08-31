%define dir /usr/libexec/argo/probes/igtf

Summary: ARGO probes for IGTF CA distribution validation
Name: argo-probe-igtf
Version: 2.0.0
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: nagios-common

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 src/*  ${RPM_BUILD_ROOT}%{dir}
install --directory --mode 770 ${RPM_BUILD_ROOT}/var/spool/argo/probes/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}
%attr(0770,nagios,nagios) /var/spool/argo/probes/%{name}

%changelog
* Mon Feb 1 2021 Emir Imamagic <eimamagi@srce.hr> - 1.5.0-1%{?dist}
- Changes from ARGO central instances
* Mon Dec 19 2016 Emir Imamagic <eimamagi@srce.hr> - 1.4.0-1%{?dist}
- Changes from ARGO central instances
* Sat Apr 9 2016 Emir Imamagic <eimamagi@srce.hr> - 1.3.0-1%{?dist}
- Added support for OCCI endpoints
- Added exception for NGI_FRANCE
* Thu Mar 24 2016 Emir Imamagic <eimamagi@srce.hr> - 1.2.0-1%{?dist}
- Added spool directory for IGTF metadata files
* Tue Mar 8 2016 Emir Imamagic <eimamagi@srce.hr> - 1.1.0-1%{?dist}
- Added new CA probe
* Fri Sep 18 2015 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version of Nagios plugins for IGTF CA distribution validation
