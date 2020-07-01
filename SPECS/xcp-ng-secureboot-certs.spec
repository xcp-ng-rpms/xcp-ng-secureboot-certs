Name:           xcp-ng-secureboot-certs
Version:        1.0.0
Release:        2
Summary:        Dummy package to solve dependencies
# License covers this spec file
License:        GPLv2
URL:            https://xcp-ng.org

BuildArch:      noarch

Provides:       secureboot-certificates

%description
This package is empty.
Its purpose is to fulfill varstored's dependencies.

%files

%changelog
* Wed Jul 01 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-2
- Rebuild for XCP-ng 8.2

* Mon Jan 20 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-1
- Initial package

