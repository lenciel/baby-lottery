#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

def get_response_code(reason, *args):
    #
    # define ajax request return codes
    #
    # 'errmsg' can be parameterized, e.g. 'import_download_flux_excel_province_not_exist'
    # get_response_code('import_download_flux_excel_province_not_exist', 12, u'未知省')
    #
    response_codes = {
                     "success": {"ret": 0, "errmsg": u"成功"},
                     "email_already_used" : {"ret": 4001, "errmsg": u"您填写的email已经被使用了"},
                    }

    """
    返回response_codes中reason对应的值的深度拷贝。
    如果返回值需要添加额外的key，则需要使用这个方法来获得对象的深度拷贝以避免修改response_codes这个全局变量。

    \param reason response_codes的key，如果"success"
    """
    ret = copy.deepcopy(response_codes[reason])
    ret['errmsg'] = ret['errmsg'] % args
    return ret
