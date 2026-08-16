from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOBAL_ASSIGNMENT = "SOONG_CONFIG_qtidisplay_composer_version"
LOCAL_NAMESPACE = "qtidisplay_sm8850"


def test_sm8850_composer_version_is_namespace_local() -> None:
    product = (ROOT / "config/display-product.mk").read_text(encoding="utf-8")
    composer = (ROOT / "composer/Android.bp").read_text(encoding="utf-8")
    qmaa = (ROOT / "qmaa/Android.bp").read_text(encoding="utf-8")

    assert GLOBAL_ASSIGNMENT not in product
    assert f"SOONG_CONFIG_{LOCAL_NAMESPACE}_composer_version" in product
    assert (
        f'soong_config_variable("{LOCAL_NAMESPACE}", "composer_version")'
        in composer
    )
    assert f'config_namespace: "{LOCAL_NAMESPACE}"' in composer
    assert f'config_namespace: "{LOCAL_NAMESPACE}"' in qmaa
