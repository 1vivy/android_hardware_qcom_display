# PROJECT KNOWLEDGE BASE
**Project:** android_hardware_qcom_display
**Seeded-at-ref:** oneplus/lineage-23.2-caf-sm8850
**Seeded-at-oid:** ad047687f2287768cb1b70cf9340981a53b25b5e
**Seeded-at-date:** 2026-08-14
**Generated-policy-sha256:** 831fceec497e89cad3d18f57f71d7d9fbc2bf2498062efbc079821f326bd17f0

## UPSTREAM DISTILLATION

### Scope and ownership

This is the QCOM SM8850 display HAL stack. It owns Composer3 integration, gralloc, display configuration and metadata libraries, tone mapping, CEC, lights, initialization, and QCOM display services. Framework composition and scheduling remain in SurfaceFlinger; device panel-feature ioctl/sysfs policy belongs to its dedicated panel HAL rather than being duplicated here.

All path guidance below is `CURRENT_PATH` truth at the seeded OID, which is also this carrier's delivery parent. There are no seed-only path or command claims in this guide.

### Build graph and module map

- `Android.bp` establishes the repository namespace and shared defaults. `config/display-product.mk`, `config/display-board.mk`, `config/display-modules.mk`, and `config/display-techpack.mk` select product-facing modules.
- `composer/` is the Composer3 implementation and service build boundary. Keep mode timing, expected-present, layer validation, and hardware-composer state coherent there.
- `composer_test_service/` is the focused Composer test-service surface; use it for contract behavior rather than introducing device-only test hooks into production code.
- `gralloc/` owns buffer allocation and mapper integration. Metadata contracts shared with composition live in `libqdmetadata/` and `libqdutils/`.
- `gpu_tonemapper/` owns QCOM GPU tone-mapping support. Do not move color-transform or panel-seed ownership into it.
- `libdisplayconfig/`, `libqservice/`, `oem_services/`, and `services/` expose focused QCOM control/service boundaries; preserve ABI and distinguish diagnostics/configuration from hardware state ownership.
- `init/` packages display init modules. `hdmi_cec/` and `dp_cec/` own their respective CEC paths; `liblight/` owns the light HAL integration.
- `hwfence_client/`, `libhistogram/`, and `libubwcp/` are low-level support libraries whose availability and header exports are controlled by local build files.

### Interfaces, policy, and extension boundaries

The seed carries no local sepolicy tree. Service changes therefore require matching init/VINTF/product and policy work in their owning repositories; an rc or XML module alone is not proof of registration. Keep Composer3 contracts standard and typed. Device-specific panel IDs, packed arguments, sysfs paths, or firmware revisions must not enter Composer or public display configuration APIs.

For adaptive refresh, Composer owns real mode metadata and expected-present delivery. A fallback framework policy may not forge Composer support, and a panel-feature service may not become a second mode-timing writer. Preserve gralloc/composer metadata compatibility across QSSI and vendor boundaries.

### Verification and conventions

Each subsystem has a local `Android.bp`; verify the changed module and its direct service/client tests, then validate product selection through `config/`. Composer or gralloc work needs the corresponding VTS/integration surface; build success does not prove a real mode transition or fence correctness.

Subjects use scoped imperative forms such as `display: ...`, `composer: ...`, and `qmaa: ...`. Keep changes narrow, preserve local C++ style, and avoid mixing compiler/tag-update cleanup with functional display behavior.

## OUR DELTAS

None at seed. Later entries must name topic commit OIDs and must not rewrite upstream truth.
