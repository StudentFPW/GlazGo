import { IAuthData } from '../modules/IAuth'
import { IRegQueryData, IRegResponseData } from '../modules/IReg'
import decamelizeKeys from 'decamelize-keys'
import baseApi from './BaseApi'

const authApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        registration: build.mutation<IRegResponseData, IRegQueryData>({
            query: (regData) => ({
                url: '/auth/reg/',
                method: 'POST',
                body: JSON.stringify(decamelizeKeys(regData))
            })
        }),
        login: build.mutation<IRegResponseData, IAuthData>({
            query: (authData) => ({
                url: '/auth/login/',
                method: 'POST',
                body: JSON.stringify(authData)
            }),
            // transformErrorResponse: (response) => response.data
        }),
        logout: build.mutation({
            query: () => ({
                url: '/auth/logout/',
                method: 'POST',
                credentials: 'include'
            })
        }),
        checkAuth: build.mutation({
            query: () => ({
                url: '/auth/token/refresh/',
                method: 'POST',
                credentials: 'include'
            })
        })
    })
})

export default authApi