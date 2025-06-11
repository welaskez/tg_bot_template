from dishka import Provider, Scope, provide

from core.feature.registry import FeatureRegistry


class FeatureProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_feature_registry(self) -> FeatureRegistry:
        return FeatureRegistry()
