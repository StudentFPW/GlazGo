import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import authReduser from './redusers/authSlice'
import baseApi from '../services/BaseApi';

export const store = configureStore({
  reducer: {
    auth: authReduser,
    [baseApi.reducerPath]: baseApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(baseApi.middleware),
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
