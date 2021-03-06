// @ts-nocheck
import { ApplyPluginsType, dynamic } from '/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/node_modules/@umijs/runtime';
import { plugin } from './plugin';

const routes = [
  {
    "path": "/xadmin/login",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__UserLayout' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/layouts/UserLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "name": "login",
        "path": "/xadmin/login",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__UserLogin' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/TyAdminBuiltIn/UserLogin'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "path": "/xadmin/",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__SecurityLayout' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/layouts/SecurityLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "path": "/xadmin/",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__BasicLayout' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/layouts/BasicLayout'), loading: require('@/components/PageLoading/index').default}),
        "authority": [
          "admin",
          "user"
        ],
        "routes": [
          {
            "name": "Home",
            "path": "/xadmin/index",
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__DashBoard' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/TyAdminBuiltIn/DashBoard'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "path": "/xadmin/",
            "redirect": "/xadmin/index",
            "exact": true
          },
          {
            "name": "???????????????",
            "icon": "BarsOutlined",
            "path": "/xadmin/auth",
            "routes": [
              {
                "name": "??????",
                "path": "/xadmin/auth/permission",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__PermissionList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/PermissionList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "???",
                "path": "/xadmin/auth/group",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GroupList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/GroupList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "????????????",
            "icon": "BarsOutlined",
            "path": "/xadmin/users",
            "routes": [
              {
                "name": "????????????",
                "path": "/xadmin/users/user_profile",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserProfileList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/UserProfileList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/users/verify_code",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__VerifyCodeList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/VerifyCodeList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "????????????",
            "icon": "BarsOutlined",
            "path": "/xadmin/goods",
            "routes": [
              {
                "name": "????????????",
                "path": "/xadmin/goods/goods_category",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GoodsCategoryList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/GoodsCategoryList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/goods/goods_category_brand",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GoodsCategoryBrandList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/GoodsCategoryBrandList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/goods/goods",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GoodsList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/GoodsList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/goods/goods_image",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GoodsImageList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/GoodsImageList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/goods/banner",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__BannerList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/BannerList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/goods/index_ad",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__IndexAdList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/IndexAdList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/goods/hot_search_words",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__HotSearchWordsList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/HotSearchWordsList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "????????????",
            "icon": "BarsOutlined",
            "path": "/xadmin/trade",
            "routes": [
              {
                "name": "????????????",
                "path": "/xadmin/trade/shopping_cart",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__ShoppingCartList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/ShoppingCartList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/trade/order_info",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__OrderInfoList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/OrderInfoList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/trade/order_goods",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__OrderGoodsList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/OrderGoodsList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "????????????",
            "icon": "BarsOutlined",
            "path": "/xadmin/user_operation",
            "routes": [
              {
                "name": "????????????",
                "path": "/xadmin/user_operation/user_fav",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserFavList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/UserFavList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/user_operation/user_address",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserAddressList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/UserAddressList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "????????????",
                "path": "/xadmin/user_operation/user_leaving_message",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserLeavingMessageList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/AutoGenPage/UserLeavingMessageList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "TyadminBuiltin",
            "icon": "VideoCamera",
            "path": "/xadmin/sys",
            "routes": [
              {
                "name": "TyAdminLog",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminSysLogList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/TyAdminBuiltIn/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdminVerify",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminEmailVerifyRecordList' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/TyAdminBuiltIn/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "passwordModify",
            "path": "/xadmin/account/change_password",
            "hideInMenu": true,
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__ChangePassword' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/TyAdminBuiltIn/ChangePassword'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          }
        ]
      },
      {
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/Users/mtianyan/tyRepos/Python/VueDjangoAntdProBookShop/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
    "exact": true
  }
];

// allow user to extend routes
plugin.applyPlugins({
  key: 'patchRoutes',
  type: ApplyPluginsType.event,
  args: { routes },
});

export { routes };
