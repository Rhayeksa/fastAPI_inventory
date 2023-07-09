import math


async def pagination(pageSize, totalData, currentPage):
    return {
        "pageSize": pageSize,
        "totalData": totalData,
        "totalPage": math.ceil(totalData/pageSize),
        "currentPage": currentPage
    }
