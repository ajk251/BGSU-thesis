def melt(
    frame: DataFrame,
    id_vars=None,
    value_vars=None,
    var_name=None,
    value_name="value",
    col_level=None,
    ignore_index: bool = True,
) -> DataFrame:
    # If multiindex, gather names of columns on all level for checking presence
    # of `id_vars` and `value_vars`
    if isinstance(frame.columns, MultiIndex):
        cols = [x for c in frame.columns for x in c]
    else:
        cols = list(frame.columns)

    if value_name in frame.columns:
        warnings.warn(
            "This dataframe has a column name that matches the 'value_name' column "
            "name of the resulting Dataframe. "
            "In the future this will raise an error, please set the 'value_name' "
            "parameter of DataFrame.melt to a unique name.",
            FutureWarning,
            stacklevel=find_stack_level(),
        )

    if id_vars is not None:
        if not is_list_like(id_vars):
            id_vars = [id_vars]
        elif isinstance(frame.columns, MultiIndex) and not isinstance(id_vars, list):
            raise ValueError(
                "id_vars must be a list of tuples when columns are a MultiIndex"
            )
        else:
            # Check that `id_vars` are in frame
            id_vars = list(id_vars)
            missing = Index(com.flatten(id_vars)).difference(cols)
            if not missing.empty:
                raise KeyError(
                    "The following 'id_vars' are not present "
                    f"in the DataFrame: {list(missing)}"
                )
    else:
        id_vars = []

    if value_vars is not None:
        if not is_list_like(value_vars):
            value_vars = [value_vars]
        elif isinstance(frame.columns, MultiIndex) and not isinstance(value_vars, list):
            raise ValueError(
                "value_vars must be a list of tuples when columns are a MultiIndex"
            )
        else:
            value_vars = list(value_vars)
            # Check that `value_vars` are in frame
            missing = Index(com.flatten(value_vars)).difference(cols)
            if not missing.empty:
                raise KeyError(
                    "The following 'value_vars' are not present in "
                    f"the DataFrame: {list(missing)}"
                )
        if col_level is not None:
            idx = frame.columns.get_level_values(col_level).get_indexer(
                id_vars + value_vars
            )
        else:
            idx = algos.unique(frame.columns.get_indexer_for(id_vars + value_vars))
        frame = frame.iloc[:, idx]
    else:
        frame = frame.copy()

    if col_level is not None:  # allow list or other?
        # frame is a copy
        frame.columns = frame.columns.get_level_values(col_level)

    if var_name is None:
        if isinstance(frame.columns, MultiIndex):
            if len(frame.columns.names) == len(set(frame.columns.names)):
                var_name = frame.columns.names
            else:
                var_name = [f"variable_{i}" for i in range(len(frame.columns.names))]
        else:
            var_name = [
                frame.columns.name if frame.columns.name is not None else "variable"
            ]
    if isinstance(var_name, str):
        var_name = [var_name]

    N, K = frame.shape
    K -= len(id_vars)

    mdata = {}
    for col in id_vars:
        id_data = frame.pop(col)
        if is_extension_array_dtype(id_data):
            if K > 0:
                id_data = concat([id_data] * K, ignore_index=True)
            else:
                # We can't concat empty list. (GH 46044)
                id_data = type(id_data)([], name=id_data.name, dtype=id_data.dtype)
        else:
            # error: Incompatible types in assignment (expression has type
            # "ndarray[Any, dtype[Any]]", variable has type "Series")
            id_data = np.tile(id_data._values, K)  # type: ignore[assignment]
        mdata[col] = id_data

    mcolumns = id_vars + var_name + [value_name]

    # error: Incompatible types in assignment (expression has type "ndarray",
    # target has type "Series")
    mdata[value_name] = frame._values.ravel("F")  # type: ignore[assignment]
    for i, col in enumerate(var_name):
        # asanyarray will keep the columns as an Index

        # error: Incompatible types in assignment (expression has type "ndarray", target
        # has type "Series")
        mdata[col] = np.asanyarray(  # type: ignore[assignment]
            frame.columns._get_level_values(i)
        ).repeat(N)

    result = frame._constructor(mdata, columns=mcolumns)

    if not ignore_index:
        result.index = tile_compat(frame.index, K)

    return result
