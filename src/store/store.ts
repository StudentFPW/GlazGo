import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import userApi from '../services/UserService'
import VacancyApi from '../services/VacancyService';

export const store = configureStore({
  reducer: {
    [userApi.reducerPath]: userApi.reducer,
    [VacancyApi.reducerPath]: VacancyApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(userApi.middleware, VacancyApi.middleware),
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
