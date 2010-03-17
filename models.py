"""
Unlike the built-in satchmo payment modules, we're not defining
`PAYMENT_PROCESSOR`; satchmo makes a lot of assumptions about modules with that
attribute that we, as a module outside of the `payment.modules` namespace, can't
satisfy.
"""
import config
