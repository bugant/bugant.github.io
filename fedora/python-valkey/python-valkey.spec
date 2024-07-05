Name:           python-valkey
Version:        5.1.0b7
Release:        %autorelease
Summary:        The Python interface to the Valkey key-value store
License:        MIT
URL:            https://github.com/valkey-io/valkey-py
Source:         %{url}/archive/v%{version}/python-valkey-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  valkey
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(async-timeout)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(cachetools)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)

%global _description %{expand:
This is a Python interface to the Valkey key-value store.}

%description %_description

%package -n     python3-valkey

Summary:        %{summary}

%description -n python3-valkey %_description

This is a Python 3 interface to the Valkey key-value store.


%prep
%autosetup -p1 -n valkey-py-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files valkey


%check
%pyproject_check_import
echo 'enable-module-command yes' | valkey-server --port 6379 --enable-debug-command yes - &
%pytest -m 'not onlycluster and not redismod and not ssl' -k 'not get_from_cache and not test_cache_decode_response[sentinel_setup0] and not psync'
kill %1


%files -n python3-valkey -f %{pyproject_files}
%doc CHANGES README.md


%changelog
%autochangelog
