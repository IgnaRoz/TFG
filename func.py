from dataclasses import dataclass, field
from typing import Callable, Any, Dict, Tuple


@dataclass
class func:
    """Contiene la función + sus parámetros por defecto."""
    func: Callable[..., Any]
    args: Tuple[Any, ...] = field(default_factory=tuple)
    kwargs: Dict[str, Any] = field(default_factory=dict)

    def run(self, *override_args, **override_kwargs) -> Any:
        final_args   = override_args or self.args
        final_kwargs = {**self.kwargs, **override_kwargs}
        return self.func(*final_args, **final_kwargs)
