def backend_retry(retry_count):
    # The decorator itself
    print("In backend retry")
    def backend_retry_decorator(method):
        print("backend_retry_decorator")
        # Inner method in the decorator
        def retry_method(*args, **kwargs):
            last_exc = Exception()

            print("In retry_method")

            # Try 3 times
            for _ in range(retry_count):
                print("Hello")
                try:
                    return method(*args, **kwargs)
                except Exception as e:
                    last_exc = e
            else:
                print("b")
                if last_exc:
                    print("cccc")
                    raise (last_exc)

        return retry_method

    return backend_retry_decorator



@backend_retry(5)
def print_method():
    print(f"Hello Again")